package hw2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class MailItemTest {

  private Recipient recipient;
  private MailItem mailItem;

  @BeforeEach
  void setUp() {
    recipient = new Recipient("Zoey", "Ai", "ab@test.com");
    mailItem = new MailItem(5, 5, 5, recipient);
  }

  @Test
  public void testConstructor() {
    assertEquals(5, mailItem.getWidth());
    assertEquals(5, mailItem.getHeight());
    assertEquals(5, mailItem.getDepth());
    assertEquals(recipient, mailItem.getRecipient());
  }

  @Test
  public void testConstructorInvalidWidth() {
    assertThrows(IllegalArgumentException.class, () -> new MailItem(0, 5, 5, recipient));
  }

  @Test
  public void testConstructorInvalidHeight() {
    assertThrows(IllegalArgumentException.class, () -> new MailItem(5, -5, 5, recipient));
  }

  @Test
  public void testConstructorInvalidDepth() {
    assertThrows(IllegalArgumentException.class, () -> new MailItem(5, 5, 0, recipient));
  }

  @Test
  public void testConstructorNullRecipient() {
    assertThrows(IllegalArgumentException.class, () -> new MailItem(5, 5, 5, null));
  }

  @Test
  public void testGetRecipient() {
    assertEquals(recipient, mailItem.getRecipient());
  }
}
