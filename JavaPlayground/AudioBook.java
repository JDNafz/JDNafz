public class AudioBook extends Book {
  private int runTime;

  AudioBook(String title, String author, Library library, int runTime) {
    super(title, author, 0, library);
    this.runTime = runTime;
  }

  public int getRunTime() {
    return this.runTime;
  }
}