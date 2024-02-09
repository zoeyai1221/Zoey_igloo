package hw2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class RecipientTest {

  private Recipient recipient;

  @BeforeEach
  void setUp() {
    recipient = new Recipient("Zoey", "Ai", "hw2@test.com");
  }

  @Test
  public void testConstructor() {
    assertEquals("Zoey", recipient.getFirstName());
    assertEquals("Ai", recipient.getLastName());
    assertEquals("hw2@test.com", recipient.getEmail());
  }

  @Test
  public void testToString() {
    assertEquals("Zoey Ai Email:hw2@test.com", recipient.toString());
  }

  @Test
  public void testConstructorNullFirstName() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient(null, "Ai", "hw2@test.com"));
  }

  @Test
  public void testConstructorEmptyFirstName() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient("", "Ai", "hw2@test.com"));
  }
  @Test
  public void testConstructorNullLastName() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient("Zoey", null, "hw2@test.com"));
  }

  @Test
  public void testConstructorEmptyLastName() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient("Zoey", "", "hw2@test.com"));
  }

  @Test
  public void testConstructorNullEmail() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient("Zoey", "Ai", null));
  }

  @Test
  public void testConstructorEmptyEmail() {
    assertThrows(IllegalArgumentException.class, () -> new Recipient("Zoey", "Ai", ""));
  }

  @Test
  public void testConstructorInvalidEmail() {
    assertDoesNotThrow(() -> new Recipient("Zoey", "Ai", "invalid-email"));
  }
}