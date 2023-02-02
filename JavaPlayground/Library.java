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

    public void addToLibrary(Book book) {
        books.add(book);
        available.add(book);
    }

    public boolean checkOut(Book book) {
        if (available.contains(book)) {
            available.remove(book);
            return true;
        } 
        return false;
    }

}