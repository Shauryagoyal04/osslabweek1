#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);

    int x, ans = 0;
    int j = 2;
    for (int i = 1; i <= 3; i++) {
        x = n % 10;
        n = n / 10;
        ans = ans + (x * pow(10, j));
        j--;
    }

    printf("%d\n", ans);
    return 0;
}