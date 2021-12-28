import java.util.*;

public class SplitWise {
    private List<Expense> grpExpense;
    private List<User> grpUsers;
    private Map<String, List<Split>> balanceSheet;

    SplitWise(List<User> grpUsers, List<Expense> grpExpense) {
        this.grpExpense = grpExpense;
        this.grpUsers = grpUsers;
        this.balanceSheet = getBalanceSheet();
    }

    public Map<String, List<Split>> getBalanceSheet() {
        Map<String, List<Split>> grpBalanceSheet = new HashMap<>();
        Map<String,Integer> userNetAmount = new HashMap<>();
        PriorityQueue<Split> usersWhoGet = new PriorityQueue<>(new SplitMaxComparator());
        PriorityQueue<Split> usersWhoOwe = new PriorityQueue<>(new SplitMaxComparator());

        for(Expense exp:grpExpense){
            String userWhoPaid = exp.getPaidBy();
            Integer paidAmount = exp.getPaidAmount();
            if(userNetAmount.containsKey(userWhoPaid)){
                userNetAmount.put(userWhoPaid,userNetAmount.get(userWhoPaid)+paidAmount);
            }else{
                userNetAmount.put(userWhoPaid,paidAmount);
            }
            for(Split expSplit: exp.getSplits()){
                String localUser = expSplit.getUserName();
                int localAmount = expSplit.getAmount();
                if(userNetAmount.containsKey(localUser)){
                    userNetAmount.put(localUser,userNetAmount.get(localUser)-localAmount);
                }else{
                    userNetAmount.put(localUser,-1*localAmount);
                }
            }
        }
        int netLenDen = 0;
        for(String user: userNetAmount.keySet()){
            int amount = userNetAmount.get(user);
            netLenDen += amount;
            if(amount == 0) continue;
            if(amount > 0){
                usersWhoGet.add(new Split(user,amount));
            }else{
                usersWhoOwe.add(new Split(user,-1*amount));
            }
        }
        System.out.println("net Len Den " + netLenDen);
        System.out.println("userNetAmount Map " + userNetAmount );
        System.out.println("usersWhoGet Q "+ usersWhoGet);
        System.out.println("usersWhoOwe Q "+ usersWhoOwe);
        while(!usersWhoGet.isEmpty()){
            Split userWhoGet = usersWhoGet.poll();
            String userWhoGetName = userWhoGet.getUserName();
            grpBalanceSheet.put(userWhoGetName,new ArrayList<>());
            int userWhoGetAmount = userWhoGet.getAmount();
            int amountRemaining = userWhoGetAmount;
            while(!usersWhoOwe.isEmpty() && amountRemaining > 0){
                Split userWhoOwe = usersWhoOwe.poll();
                String userWhoOweName = userWhoOwe.getUserName();
                int userWhoOweAmount = userWhoOwe.getAmount();
                if(amountRemaining >= userWhoOweAmount){
                    grpBalanceSheet.get(userWhoGetName).add(new Split(userWhoOweName,userWhoOweAmount));
                    amountRemaining -= userWhoOweAmount;
                }else{
                    grpBalanceSheet.get(userWhoGetName).add(new Split(userWhoOweName,amountRemaining));
                    usersWhoOwe.add(new Split(userWhoOweName,userWhoOweAmount-amountRemaining));
                    amountRemaining = 0;
                }
            }
        }
        System.out.println(grpBalanceSheet);
        this.balanceSheet = grpBalanceSheet;
        return balanceSheet;
    }

    public List<Expense> getGrpExpense() {
        return grpExpense;
    }

    public List<User> getGrpUsers() {
        return grpUsers;
    }

    public void setGrpExpense(List<Expense> grpExpense) {
        this.grpExpense = grpExpense;
    }

    public void setGrpUsers(List<User> grpUsers) {
        this.grpUsers = grpUsers;
    }
}
