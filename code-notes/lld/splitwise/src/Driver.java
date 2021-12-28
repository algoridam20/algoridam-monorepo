import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Driver {
    public static void main(String[] args) {
        List<User> users = new ArrayList<>();
        users.add(new User("u1"));
        users.add(new User("u2"));
        users.add(new User("u3"));
        users.add(new User("u4"));

        List<String> allUserNames = Arrays.asList("u1", "u2", "u3");

        List<Expense> expenses = new ArrayList<>();
        expenses.add(ExpenseGenerator.generator("exp1","u1", 90, "no" ,allUserNames, ExpenseType.EXACT, Arrays.asList(10, 30, 50)));
        expenses.add(ExpenseGenerator.generator("exp1","u2", 60, "no" ,allUserNames, ExpenseType.EQUAL, new ArrayList<>()));
        expenses.add(ExpenseGenerator.generator("exp1","u3", 90, "no" ,allUserNames, ExpenseType.PERCENT, Arrays.asList(10, 40, 50)));

        expenses.add(ExpenseGenerator.generator("exp1","u1", 90, "notes1" ,Arrays.asList("u2"), ExpenseType.EQUAL, new ArrayList<>()));
        expenses.add(ExpenseGenerator.generator("exp2","u2", 90, "notes2" ,Arrays.asList("u3"), ExpenseType.EQUAL, new ArrayList<>()));
        expenses.add(ExpenseGenerator.generator("exp3","u3", 90, "notes3" ,Arrays.asList("u1"), ExpenseType.EQUAL, new ArrayList<>()));
        expenses.add(ExpenseGenerator.generator("exp3","u4", 12, "notes3" ,Arrays.asList("u1"), ExpenseType.EQUAL, new ArrayList<>()));
        SplitWise swGRP = new SplitWise(users,expenses);
    }
}
