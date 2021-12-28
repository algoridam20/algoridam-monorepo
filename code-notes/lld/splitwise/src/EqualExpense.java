import java.util.ArrayList;
import java.util.List;

public class EqualExpense extends Expense {

    public EqualExpense(String title, String paidBy, int paidAmount, String notes, List<String> splitUsers, ExpenseType type, List<Integer> splitParam) {
        super(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
        splitCalculateAndSet();
    }

    @Override
    protected void splitCalculateAndSet(){
        int totalSplits = splitUsers.size();
        int splitValue = paidAmount/totalSplits;
        splits = new ArrayList<>();
        for(String user:splitUsers){
            splits.add(new Split(user,splitValue));
        }
        splits.get(0).setAmount(splitValue + paidAmount - splitValue*totalSplits);
    }

}
