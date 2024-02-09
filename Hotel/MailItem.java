package hw2;

/**
 * Represents a mail item.
 */
public class MailItem {

  // Minimum width allowed for a locker, in inches
  public static final int MIN_MAIL_WIDTH = 1;
  // Minimum height allowed for a locker, in inches
  public static final int MIN_MAIL_HEIGHT = 1;
  // Minimum depth allowed for a locker, in inches
  public static final int MIN_MAIL_DEPTH = 1;

  private final int width;
  private final int height;
  private final int depth;
  private final Recipient recipient;

  /**
   * Constructs a new MailItem with the given dimensions and recipient.
   * @param width the width of the mail item
   * @param height the height of the mail item
   * @param depth the depth of the mail item
   * @param recipient the recipient of the mail item
   * @throws IllegalArgumentException if any of the dimensions are less than 1 or if the recipient is null
   */
  public MailItem(int width, int height, int depth, Recipient recipient) {
    if (width < MIN_MAIL_WIDTH || height < MIN_MAIL_HEIGHT || depth < MIN_MAIL_DEPTH || recipient == null) {
      throw new IllegalArgumentException("Dimensions must be greater than or equal to 1, and recipient cannot be null");
    }
    this.width = width;
    this.height = height;
    this.depth = depth;
    this.recipient = recipient;
  }

  /**
   * Gets the width of the mail item.
   * @return the width
   */
  public int getWidth() {
    return width;
  }

  /**
   * Gets the depth of the mail item.
   * @return the depth
   */
  public int getDepth() {
    return depth;
  }

  /**
   * Gets the height of the mail item.
   * @return the height
   */
  public int getHeight() {
    return height;
  }

  /**
   * Gets the recipient of the mail item.
   * @return the recipient
   */
  public Recipient getRecipient() {
    return recipient;
  }
}
