import java.util.ArrayList;
import java.util.List;

public class PercentExpense extends Expense {

    public PercentExpense(String title, String paidBy, int paidAmount, String notes, List<String> splitUsers, ExpenseType type, List<Integer> splitParam) {
        super(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
        splitCalculateAndSet();
    }

    @Override
    protected void splitCalculateAndSet(){
        int totalSplits = splitUsers.size();
        splits = new ArrayList<>();
        int sum = 0;
        for(int i=0;i<totalSplits;i++){
            int splitValue = (splitParam.get(i)*paidAmount)/100;
            splits.add(new Split(splitUsers.get(i),splitValue));
            sum += splitValue;
        }
        splits.get(0).setAmount(splits.get(0).getAmount() + paidAmount - sum);
    }

}
