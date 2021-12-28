import java.util.List;
import java.util.UUID;

public abstract class Expense {
    protected UUID id;
    protected List<Split> splits;

    protected String title;
    protected String paidBy;
    protected int paidAmount;
    protected String notes;
    protected List<String> splitUsers;
    protected ExpenseType type;
    protected List<Integer> splitParam;

    public Expense(String title, String paidBy, int paidAmount, String notes, List<String> splitUsers, ExpenseType type, List<Integer> splitParam) {
        this.id = UUID.randomUUID();
        this.title = title;
        this.paidBy = paidBy;
        this.paidAmount = paidAmount;
        this.notes = notes;
        this.splitUsers = splitUsers;
        this.type = type;
        this.splitParam = splitParam;

    }

    protected void splitCalculateAndSet(){
        // default;
    }

    protected boolean validator(){
        int total = paidAmount;
        for(Split split: splits){
            total -= split.getAmount();
        }
        return total == 0;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setPaidBy(String paidBy) {
        this.paidBy = paidBy;
    }

    public void setPaidAmount(int paidAmount) {
        this.paidAmount = paidAmount;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public void setSplits(List<Split> splits) {
        this.splits = splits;
    }

    public UUID getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getPaidBy() {
        return paidBy;
    }

    public int getPaidAmount() {
        return paidAmount;
    }

    public String getNotes() {
        return notes;
    }

    public List<Split> getSplits() {
        return splits;
    }
}
