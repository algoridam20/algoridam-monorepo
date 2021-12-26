import java.util.*;

public class SnakeAndLadder {

    static class Dice {
        private int minFaces = 1;
        private int maxFaces = 100;
        private Random rand;
        private int faces;
        private boolean isFair = true;

        Dice(int faces) {
            if (faces < minFaces || faces > maxFaces) {
                System.out.println("Invalid Dice !");
                System.out.println("Using default dice of 6 sides");
                this.faces = 6;
                this.isFair = true;
            }
            rand = new Random();
            this.faces = faces;
        }

        public int getFaces() {
            return this.faces;
        }

        public int rollDice() {
            int randomNum = rand.nextInt(faces) + 1;
            System.out.println("Rolling Dice ..... " + randomNum);
            return randomNum;
        }
    }

    static class Player {
        private String playerName;
        private String playerId;
        private List<Integer> positions;
        private boolean isWinner;

        Player(String name) {
            this.playerName = name;
            this.playerId = UUID.randomUUID().toString();
            this.positions = new ArrayList<Integer>();
            this.positions.add(0);
            this.isWinner = false;
        }

        public String getPlayerName() {
            return playerName;
        }
        public String getPlayerId() {
            return playerId;
        }
        public boolean getIsWinner() {
            return isWinner;
        }
        public void setWinner() {
            this.isWinner = true;
        }
        public List<Integer> getPositions() {
            return positions;
        }
        public int getLastPosition() {
            return positions.get(positions.size() - 1);
        }
        public void setNextPosition(int nextPos) {
            positions.add(nextPos);
        }
    }

    static class Board {
        private int boardSize = 101;
        private List<Integer> cells;

        Board(List<List<Integer>> snakes, List<List<Integer>> ladder) {
            cells = new ArrayList<>(Collections.nCopies(boardSize, 0));

            for (int i = 0; i < snakes.size(); i++) {
                int head = snakes.get(i).get(0);
                int tail = snakes.get(i).get(1);
                int val = tail - head;
                cells.set(head, val);
            }
            for (int i = 0; i < ladder.size(); i++) {
                int head = ladder.get(i).get(0);
                int tail = ladder.get(i).get(1);
                int val = head - tail;
                cells.set(tail, val);
            }
        }

        public int getMaxIndex() {
            return boardSize - 1;
        }

        public int getNextJump(int index) {
            if (index >= boardSize ||
                    index < 1) {
                System.out.println("Index out of bound, Player on same Position");
                return 0;
            }
            return cells.get(index);
        }

    }

    static class Game {
        private Dice gameDice;
        private Board gameBoard;
        private Queue<Player> Players;

        Game(int diceFaces, List<String> players, List<List<Integer>> snakes, List<List<Integer>> ladder) {
            this.Players = new LinkedList<>();
            for (int i = 0; i < players.size(); i++) {
                this.Players.add(new Player(players.get(i)));
            }
            this.gameDice = new Dice(diceFaces);
            this.gameBoard = new Board(snakes, ladder);
        }

        private Player getCurrPlayer() {
            Player currPlayer = Players.poll();
            return currPlayer;
        }

        private int makeMove(Player currPlayer, int currDiceVal) {
            int currIndex = currPlayer.getLastPosition();
            int nextPossibleIndex = currIndex + currDiceVal;


            while (gameBoard.getNextJump(nextPossibleIndex) != 0) {
                nextPossibleIndex += gameBoard.getNextJump(nextPossibleIndex);
            }

            if (nextPossibleIndex > gameBoard.getMaxIndex()) {
                nextPossibleIndex = currIndex;
            } else if (nextPossibleIndex == gameBoard.getMaxIndex()) {
                System.out.println("Player :" + currPlayer.getPlayerName() + " Won the Game !");
                currPlayer.setWinner();
            }
            currPlayer.setNextPosition(nextPossibleIndex);
            Players.add(currPlayer);
            if (currPlayer.getIsWinner()) {
                for (Player player : Players) {
                    System.out.println("Player :" + player.getPlayerName() + " " + player.getPlayerId());
                    System.out.println(player.getPositions());
                }
            }
            System.out.println(currPlayer.getPlayerName() + " reached cell :" + nextPossibleIndex + " from " + currIndex + "\n");
            return nextPossibleIndex;
        }

        public int playNextMove() {
            Player currPlayer = getCurrPlayer();
            System.out.println("\n" + currPlayer.getPlayerName()+"'s Turn");
            int currDiceVal = gameDice.rollDice();
            return makeMove(currPlayer, currDiceVal);
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> snakes = new ArrayList<>();
        snakes.add(Arrays.asList(98, 14));
        snakes.add(Arrays.asList(50, 21));
        snakes.add(Arrays.asList(13, 7));

        List<List<Integer>> ladders = new ArrayList<>();
        ladders.add(Arrays.asList(14, 4));
        ladders.add(Arrays.asList(78,14));
        ladders.add(Arrays.asList(56, 23));
        ladders.add(Arrays.asList(99, 88));

        List<String> playerNames = Arrays.asList("Ridam", "Mini", "Tinku");

        Game game = new Game(7, playerNames, snakes, ladders);

        while (game.playNextMove() != 100) {
        }
    }
}


// javac SnakeAndLadder.java && java SnakeAndLadder
