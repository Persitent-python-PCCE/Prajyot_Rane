import java.util.Arrays;

class Rearrange
{
    public static void main(String[] args)
    {
        int[] arr={10 ,20, 30, 40, 50};
        String st="DADAA";
        int[] res =new int[arr.length];
        int index=0;
        for(int i=0;i<arr.length;i++)
        {                
                        if(st.charAt(i)=='A')
                        {
                                res[index]=arr[i];
                                index++;
                        }
        }
        for(int i=0;i<arr.length;i++)
        {
                if(st.charAt(i)=='D')
                {
                        res[index]=arr[i];
                        index++;
                }
        }
        System.out.println(Arrays.toString(res));
}
}
