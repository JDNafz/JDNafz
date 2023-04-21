// import java.util.ArrayList;

public class Book {
  private String title;
  private String author;
  private int pageCount;
  private String location;
  private String libraryHome;
//   public static ArrayList<Book> books = new ArrayList<Book>();
  

  Book(String title, String author, int pageCount, Library library){
    this.title = title;
    this.author = author;
    this.pageCount = pageCount;
    this.location = library.getName();
    this.libraryHome = library.getName();
    library.addToLibrary(this);
  }
    
  public void getInfo(){
    System.out.printf("%s by %s", this.getTitle(), this.getAuthor());
  }

  public String toString() {
    return String.format("%s by %s[%d] pages, >%s.\n", this.title, this.author, this.pageCount, this.libraryHome);
  }
  public String getTitle() {
    return this.title;
  }
  public String getAuthor() {
    return this.author;
  }

public void checkedOutBy(String user) {
    this.location = user;
}

public void returnedTo(Library library) {
    if (library.returnBook(this)) {
        this.location = library.getName();
    }
    else {
        System.out.printf("%s belongs to %s, not %s please return it there. \n", this.title, this.libraryHome, library.getName());
        }
    }

public String getLocation() {
    return this.location.toString();
}
  
}