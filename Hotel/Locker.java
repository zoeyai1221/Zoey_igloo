package hw2;

/**
 * Represents a locker for storing mail items.
 */
public class Locker {

  // Magic Number replacement
  public static final int MIN_LOCKER_WIDTH = 1;
  public static final int MIN_LOCKER_HEIGHT = 1;
  public static final int MIN_LOCKER_DEPTH = 1;


  private final int maxWidth;
  private final int maxHeight;
  private final int maxDepth;
  private MailItem mailItem;

  /**
   * Constructs a new Locker with the given dimensions.
   * @param maxWidth the maximum width of the locker
   * @param maxHeight the maximum height of the locker
   * @param maxDepth the maximum depth of the locker
   * @throws IllegalArgumentException if any of the dimensions are less than 1
   */
  public Locker(int maxWidth, int maxHeight, int maxDepth) {
    if (maxWidth < MIN_LOCKER_WIDTH || maxHeight < MIN_LOCKER_HEIGHT || maxDepth < MIN_LOCKER_DEPTH) {
      throw new IllegalArgumentException("Dimensions must be greater than or equal to 1");
    }
    this.maxWidth = maxWidth;
    this.maxHeight = maxHeight;
    this.maxDepth = maxDepth;
  }

  /**
   * Gets the maxWidth of the locker.
   * @return the maxWidth
   */
  public int getMaxWidth() {
    return maxWidth;
  }

  /**
   * Gets the maxHeight of the locker.
   * @return the maxHeight
   */
  public int getMaxHeight() {
    return maxHeight;
  }

  /**
   * Gets the maxDepth of the locker.
   * @return the maxDepth
   */
  public int getMaxDepth() {
    return maxDepth;
  }

  /**
   * Gets the mailItem of the locker.
   * @return the mailItem
   */
  public MailItem getMailItem() {
    return mailItem;
  }

  /**
   * Adds a mail item to the locker.
   * @param item the mail item to add
   * @throws IllegalStateException if the locker is already occupied or the item dimensions exceed the locker dimensions
   */
  public void addMail(MailItem item) {
    if (mailItem != null || item.getWidth() > maxWidth || item.getHeight() > maxHeight || item.getDepth() > maxDepth) {
      throw new IllegalStateException("Cannot add mail item to locker");
    }
    mailItem = item;
  }

  /**
   * Picks up a mail item from the locker if it matches the recipient.
   * @param recipient the recipient of the mail item
   * @return the mail item if it matches the recipient, null otherwise
   */
  public MailItem pickupMail(Recipient recipient) {
    if (mailItem != null && mailItem.getRecipient().equals(recipient)) {
      MailItem item = mailItem;
      mailItem = null;
      return item;
    }
    return null;
  }
}
