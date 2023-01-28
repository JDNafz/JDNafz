// import java.util.ArrayList;

public class Book {
  private String title;
  private String author;
  private int pageCount;
//   public static ArrayList<Book> books = new ArrayList<Book>();
  

  Book(String title, String author, int pageCount){
    this.title = title;
    this.author = author;
    this.pageCount = pageCount;
    books.add(this);
  }
    
  public void getInfo(){
    System.out.printf("%s by %s", this.getTitle(), this.getAuthor());
  }

  public String toString() {
    return String.format("%s by %s[%d] pages\n", this.title, this.author, this.pageCount);
  }
  public String getTitle() {
    return this.title;
  }
  public String getAuthor() {
    return this.author;
  }
  
}