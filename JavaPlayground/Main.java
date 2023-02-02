// user1 tries to checkout book checkouted by other user.
//user tries to checkout from two dif libs >mark checkedout books with a library tag


class Main {
    public static void main(String[] args) {
        Library loringParkLibrary = new Library("loringParkLibrary");
        Library central = new Library("central");
        User user1 = new User("JD Naf","1992-01-24",loringParkLibrary);
      
        Book rainbows = new Book("Rainbows on Fire","Kill Joy Frenkins",69, loringParkLibrary);
        AudioBook skysounds = new AudioBook("Skysounds","Skrillex", loringParkLibrary, 60 );
        
        EBook bandanas = new EBook("Bandanas","Tom Hanks",420, central, "mp3");
        
        
        // System.out.println(bandanas.toString());
        
        
        user1.borrow(rainbows);
        user1.borrow(bandanas,central);
        // System.out.printf("user1's Books: %s \n", user1.getBooks());

        // System.out.printf("Books from LPL: %s \n", loringParkLibrary.getBooks().toString());
        loringParkLibrary.printBooks();
        central.printBooks();

        // System.out.printf("Books from Central: %s \n", central.getBooks().toString());
        

    }
}