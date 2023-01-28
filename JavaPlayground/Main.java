// import java.time.LocalDate;

class Main {
  public static void main(String[] args) {
    //User user1 = new User("JD Naf","1992-01-24");

    Book rainbows = new Book("Rainbows on Fire","Kill Joy Frenkins",69);
    EBook bandanas = new EBook("Bandanas","Tom Hanks",420,"mp3");
    AudioBook skysounds = new AudioBook("Skysounds","Skrillex", 60);

    System.out.println(bandanas.toString());
    

    // user1.borrow(book1);
    // user1.borrow(book2);

    
    
    // System.out.printf("%s was born back in %s and they are %d years old.", user1.getName(), user1.getBirthDay(), user1.age());

    // System.out.printf("%s has borrowed these books:\n%s \n", user1.getName(), user1.borrowedBooks());

    // System.out.printf("%s by %s", book1.getTitle(),book2.getAuthor());
  }
}