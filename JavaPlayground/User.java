import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
    private String name;
    private LocalDate birthDay;
    private ArrayList<Book> books;
    private Library library;

    //constructor method
    User(String nameVar, String birthDay, Library library){
        this.name = nameVar;
        this.birthDay = LocalDate.parse(birthDay);
        this.library = library;
        this.books = new ArrayList<>();
    }

    public String getName() {
        return this.name;
    }

    public String getBirthDay() {
        return this.birthDay.toString();
    }
    public void borrow(Book book, Library library) {
        if (library.checkOut(book)) {
            this.books.add(book);
        } 
        else {
            System.out.println("NOPE GET FUCKED GET YOUR OWN BOK!");
        }    

    }

    // uses default library if no library is provided
    public void borrow(Book book) {
        borrow(book, library);    
        }

    public String getBooks() {
        return books.toString();
    }

    public int age() {
        int age = Period.between(this.birthDay, LocalDate.now()).getYears();

        return age;
    }
}