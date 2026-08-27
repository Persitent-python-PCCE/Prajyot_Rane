import java.util.Arrays;
class LongestSeq {
    public static void main(String[] args) {
        int[] arr = {100, 43, 434, 2};
        int len = arr.length;
        int count = 1;
        Arrays.sort(arr);
        for (int i = 0; i < len - 1; i++) {
            if (arr[0] + 1 != arr[1]) {
                System.out.println("No output");
                exit;
            }
        if (arr[i] + 1 == arr[i + 1]) {
            count++;
        }
    }
                for ( int i=0;i<count;i++)
                {
                    System.out.println(arr[i]);
                }
    }
}