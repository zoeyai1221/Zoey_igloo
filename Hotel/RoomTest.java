package hw2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class RoomTest {

  private Room singleRoom;
  private Room doubleRoom;
  private Room familyRoom;

  @BeforeEach
  void setUp() {
    singleRoom = new SingleRoom(100);
    doubleRoom = new DoubleRoom(150);
    familyRoom = new FamilyRoom(200);
  }

  @Test
  public void testIsAvailable() {
    assertTrue(singleRoom.isAvailable());
    assertTrue(doubleRoom.isAvailable());
    assertTrue(familyRoom.isAvailable());

    singleRoom.bookRoom(1);
    assertFalse(singleRoom.isAvailable());

    doubleRoom.bookRoom(2);
    assertFalse(doubleRoom.isAvailable());

    familyRoom.bookRoom(4);
    assertFalse(familyRoom.isAvailable());
  }

  @Test
  public void testBookRoom() {
    singleRoom.bookRoom(1);
    assertEquals(1, singleRoom.getNumberOfGuests());
    assertThrows(IllegalStateException.class, () -> singleRoom.bookRoom(2));

    doubleRoom.bookRoom(2);
    assertEquals(2, doubleRoom.getNumberOfGuests());
    assertThrows(IllegalStateException.class, () -> doubleRoom.bookRoom(3));

    familyRoom.bookRoom(4);
    assertEquals(4, familyRoom.getNumberOfGuests());
    assertThrows(IllegalStateException.class, () -> familyRoom.bookRoom(5));
  }

  @Test
  public void testGetNumberOfGuests() {
    assertEquals(0, singleRoom.getNumberOfGuests());
    assertEquals(0, doubleRoom.getNumberOfGuests());
    assertEquals(0, familyRoom.getNumberOfGuests());

    singleRoom.bookRoom(1);
    assertEquals(1, singleRoom.getNumberOfGuests());

    doubleRoom.bookRoom(2);
    assertEquals(2, doubleRoom.getNumberOfGuests());

    familyRoom.bookRoom(4);
    assertEquals(4, familyRoom.getNumberOfGuests());
  }

  @Test
  public void testGetMaxOccupancy() {
    assertEquals(1, singleRoom.getMaxOccupancy());
    assertEquals(2, doubleRoom.getMaxOccupancy());
    assertEquals(4, familyRoom.getMaxOccupancy());
  }

  @Test
  public void testGetPrice() {
    assertEquals(100, singleRoom.getPrice(), 0);
    assertEquals(150, doubleRoom.getPrice(), 0);
    assertEquals(200, familyRoom.getPrice(), 0);
  }

  // Tests for equals() method
  @Test
  void testEqualsSameObject() {
    Room room = new SingleRoom(100.0); // Initialize with any values
    assertEquals(room, room);
  }

  @Test
  void testEqualsSameProperties() {
    Room room1 = new SingleRoom(100.0);
    Room room2 = new SingleRoom(100.0);
    assertEquals(room1, room2);
  }

  @Test
  void testEqualsDifferentProperties() {
    Room room1 = new SingleRoom(100.0);
    Room room2 = new SingleRoom(150.0); // Different price
    assertNotEquals(room1, room2);
  }

  @Test
  void testEqualsNull() {
    Room room = new SingleRoom(100.0);
    assertNotEquals(null, room);
  }

  @Test
  void testEqualsDifferentType() {
    Room room = new SingleRoom(100.0);
    assertNotEquals("NA", room);
  }

  // Tests for subclasses
  @Test
  void testSingleRoomEquals() {
    SingleRoom room1 = new SingleRoom(100.0);
    SingleRoom room2 = new SingleRoom(100.0);
    assertEquals(room1, room2);
  }

  @Test
  void testDoubleRoomEquals() {
    DoubleRoom room1 = new DoubleRoom(200.0);
    DoubleRoom room2 = new DoubleRoom(200.0);
    assertEquals(room1, room2);
  }

  @Test
  void testFamilyRoomEquals() {
    FamilyRoom room1 = new FamilyRoom(300.0);
    FamilyRoom room2 = new FamilyRoom(300.0);
    assertEquals(room1, room2);
  }
}
