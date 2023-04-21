import java.util.ArrayList;

public class Library {
    private ArrayList<Book> books;
    private String name;
    private ArrayList<Book> available;
    

    Library(String name){
        this.name = name;
        this.books = new ArrayList<>();
        this.available = new ArrayList<>();
    }

    public ArrayList<Book> getBooks() {
        return books;
    }

    public void printBooks() {
        System.out.printf("%s: %s \n",this.name, getBooks().toString());
    }

    public void printAvailable() {
        if (available.isEmpty()) {
            System.out.printf("%s does not have any available books\n", this.name);
        }
        else {
            System.out.printf("%s", available.toString());
        }
    }

    public void addToLibrary(Book book) {
        books.add(book);
        available.add(book);
    }

    public boolean checkOut(Book book) {
        if (available.contains(book)) {
            available.remove(book);

            return true;
        } 
        else {
            if (books.contains(book)) {
                System.out.printf("%s has a copy of %s but it has already been checked by %s.", this.name, book, book.getLocation());
                return false;
            }
            return false;
        }
    }

    public String getName() {
        return name;
    }

    public boolean returnBook(Book book) {
        if (this.books.contains(book)) {
            available.add(book);
            return true;
        }
        else {
            return false;
        }
    }

}
