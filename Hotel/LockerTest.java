package hw2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class LockerTest {

  private Locker locker;
  private MailItem mailItem;
  private Recipient recipient;

  @BeforeEach
  void setUp() {
    locker = new Locker(10, 10, 10);
    recipient = new Recipient("Zoey", "Ai", "hw2@test.com");
    mailItem = new MailItem(5, 5, 5, recipient);
  }

  @Test
  public void testConstructor() {
    assertEquals(10, locker.getMaxWidth());
    assertEquals(10, locker.getMaxHeight());
    assertEquals(10, locker.getMaxDepth());
    assertNull(locker.getMailItem());
  }

  @Test
  public void testAddMail() {
    locker.addMail(mailItem);
    assertEquals(mailItem, locker.getMailItem());

    MailItem oversizedMail = new MailItem(20, 20, 20, recipient);
    assertThrows(IllegalStateException.class, () -> locker.addMail(oversizedMail));

    MailItem secondMail = new MailItem(5, 5, 5, recipient);
    assertThrows(IllegalStateException.class, () -> locker.addMail(secondMail));
  }

  @Test
  public void testPickupMail() {
    assertNull(locker.pickupMail(recipient));

    locker.addMail(mailItem);
    assertEquals(mailItem, locker.pickupMail(recipient));

    assertNull(locker.pickupMail(recipient));
  }
}
