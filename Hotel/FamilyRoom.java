package hw2;

/**
 * Represents a family room in a hotel.
 */
public class FamilyRoom extends Room {

  /**
   * Magic Number replacement
   */
  public static final int MAX_OCCUPANCY_FAMILY = 4;

  /**
   * Constructs a new FamilyRoom with the given price.
   * @param price the price per night for the room
   */
  public FamilyRoom(double price) {
    super(MAX_OCCUPANCY_FAMILY, price);
  }
}
