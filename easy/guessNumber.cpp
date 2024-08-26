class Solution {
public:
    int guessNumber(int n) {
        return binarySearch(0,n);
    }

    int binarySearch(int l,int h) {
        int middle = l + (h - l) / 2;
        int result = guess(middle);

        if (result == 0) {
            return middle;
        }

        if (result == 1) {
            return binarySearch(middle + 1, h);
        }

        else {
            return binarySearch(l, middle - 1);
        }

    }
};
