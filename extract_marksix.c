#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RESULTS 10000 // Sufficient for many years of results

struct Result {
    char draw[20];
    char date[20];
    int ymd;
    char balls[100];
};

int compare(const void *a, const void *b) {
    return ((struct Result*)a)->ymd - ((struct Result*)b)->ymd;
}

int main() {
    // Fetch the HTML using curl (assumes curl is installed)
    system("curl -o page.html \"https://bet.hkjc.com/marksix/results.aspx?lang=ch\"");

    // Read the fetched HTML
    FILE *fp = fopen("page.html", "r");
    if (!fp) {
        printf("Failed to open page.html\n");
        return 1;
    }
    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    char *html = malloc(size + 1);
    if (!html) {
        fclose(fp);
        return 1;
    }
    fread(html, 1, size, fp);
    html[size] = 0;
    fclose(fp);

    // Parse the HTML for results
    struct Result new_results[100];
    int num_new = 0;
    char *p = html;
    while ((p = strstr(p, "<div class=\"table-row")) != NULL) {
        // Find draw ID (e.g., 25/126 or 25/125 STU)
        char *start = strstr(p, "<a>");
        if (!start) break;
        start += 3;
        char *end = strstr(start, "</a>");
        if (!end) break;
        strncpy(new_results[num_new].draw, start, end - start);
        new_results[num_new].draw[end - start] = 0;

        // Find date
        start = strstr(end, "<div class=\"table-cell cell-date\">");
        if (!start) break;
        start += strlen("<div class=\"table-cell cell-date\">");
        end = strstr(start, "</div>");
        if (!end) break;
        strncpy(new_results[num_new].date, start, end - start);
        new_results[num_new].date[end - start] = 0;

        // Compute ymd for sorting (yyyymmdd)
        int dd, mm, yyyy;
        sscanf(new_results[num_new].date, "%d/%d/%d", &dd, &mm, &yyyy);
        new_results[num_new].ymd = yyyy * 10000 + mm * 100 + dd;

        // Find ball list and extract alts
        start = strstr(end, "<div class=\"table-cell cell-ball-list\">");
        if (!start) break;
        char balls[100] = {0};
        char *bp = balls;
        char *sep = "";
        int count = 0;
        char *ball_p = start;
        while ((ball_p = strstr(ball_p, "alt=\"")) != NULL && count < 7) {
            ball_p += 5;
            char *ball_end = strchr(ball_p, '"');
            if (!ball_end) break;
            char num[3];
            strncpy(num, ball_p, ball_end - ball_p);
            num[ball_end - ball_p] = 0;
            bp += sprintf(bp, "%s%s", sep, num);
            sep = " ";
            if (count == 5) sep = " + ";
            count++;
            ball_p = ball_end;
        }
        strcpy(new_results[num_new].balls, balls);

        num_new++;
        p = ball_p; // Advance pointer
    }
    free(html);

    // Read existing results from file
    struct Result all_results[MAX_RESULTS];
    int num_all = 0;
    FILE *out = fopen("marksix_result.txt", "r");
    if (out) {
        char line[256];
        while (fgets(line, sizeof(line), out)) {
            sscanf(line, "%s %s %[^\n]", all_results[num_all].draw, all_results[num_all].date, all_results[num_all].balls);
            int dd, mm, yyyy;
            sscanf(all_results[num_all].date, "%d/%d/%d", &dd, &mm, &yyyy);
            all_results[num_all].ymd = yyyy * 10000 + mm * 100 + dd;
            num_all++;
        }
        fclose(out);
    }

    // Add new results if not already present (check by draw ID)
    for (int i = 0; i < num_new; i++) {
        int found = 0;
        for (int j = 0; j < num_all; j++) {
            if (strcmp(all_results[j].draw, new_results[i].draw) == 0) {
                found = 1;
                break;
            }
        }
        if (!found) {
            all_results[num_all] = new_results[i];
            num_all++;
        }
    }

    // Sort all results by date ascending
    qsort(all_results, num_all, sizeof(struct Result), compare);

    // Write back to file (create if not exists)
    out = fopen("marksix_result.txt", "w");
    if (!out) {
        printf("Failed to open marksix_result.txt\n");
        return 1;
    }
    for (int i = 0; i < num_all; i++) {
        fprintf(out, "%s %s %s\n", all_results[i].draw, all_results[i].date, all_results[i].balls);
    }
    fclose(out);

    return 0;
}