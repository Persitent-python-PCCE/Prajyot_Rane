import java.util.*;
class Second_high_count
{
    public static void main(String[] args) {
        
        String st="programming";
        char max_char=' ';
        int max_count=0;

        Map<Character,Integer> st_hash=new HashMap<>();

        for(char c:st.toCharArray())
        {
            st_hash.put(c,st_hash.getOrDefault(c, 0)+1);
        }

        
        for(int count:st_hash.values())
        {
                if(count>max_count)
                {
                    max_count=count;
                }
        }
        for (char c:st.toCharArray())
        {
            if(st_hash.get(c)==max_count)
            {
                max_char=c;
                break;
            }
        }
        System.out.printf("Second Max Count Element :"+max_char+" "+max_count);
    }
}