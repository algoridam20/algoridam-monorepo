import java.util.Comparator;

public class SplitMinComparator implements Comparator<Split> {
    public int compare(Split s1, Split s2) {
        if (s1.getAmount() > s2.getAmount())
            return 1;
        else if (s1.getAmount() < s2.getAmount())
            return -1;
        return 0;
    }
}
