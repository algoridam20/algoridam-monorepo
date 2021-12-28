import java.util.ArrayList;
import java.util.List;

public class ExactExpense extends Expense {

    public ExactExpense(String title, String paidBy, int paidAmount, String notes, List<String> splitUsers, ExpenseType type, List<Integer> splitParam) {
        super(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
        splitCalculateAndSet();
    }

    @Override
    protected void splitCalculateAndSet(){
        //TODO: validate
        int totalSplits = splitUsers.size();
        splits = new ArrayList<>();
        for(int i=0;i<totalSplits;i++){
            splits.add(new Split(splitUsers.get(i),splitParam.get(i)));
        }
    }

}
