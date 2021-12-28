
import java.util.List;

public class ExpenseGenerator {
    public static Expense generator(String title, String paidBy, int paidAmount, String notes, List<String> splitUsers, ExpenseType type, List<Integer> splitParam){
        switch (type){
            case EQUAL:
                return new EqualExpense(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
            case EXACT:
                return new ExactExpense(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
            case PERCENT:
                return new PercentExpense(title, paidBy, paidAmount, notes, splitUsers, type, splitParam);
            default:
                throw new RuntimeException();
        }
    }
}
