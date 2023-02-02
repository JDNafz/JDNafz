public class EBook extends Book {
  private String format;

  EBook(String title, String author,int pageCount,Library library, String format) {
    super(title, author, pageCount, library);
    
    this.format = format;
  }

  public String getFormat() {
    return this.format;
  }
}