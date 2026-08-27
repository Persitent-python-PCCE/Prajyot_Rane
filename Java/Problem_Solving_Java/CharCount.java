import java.util.*;
class CharCount{
    public static void main(String[] args) {
        String s="aaabbccccd";
        String copy;
        int slen=s.length();
        LinkedHashSet<Character> hash=new LinkedHashSet<>();
        for(char i:s.toCharArray())
        {
            hash.add(i);
        }
        for(char st:hash)
        {
            copy=s.replace(String.valueOf(st),"");
            int count=slen-copy.length();
            System.out.printf("%s%s",st,count);
        }

                }
    }
