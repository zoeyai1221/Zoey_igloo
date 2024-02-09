package hw2;

/**
 * Represents a double room in a hotel.
 */
public class DoubleRoom extends Room {

  /**
   * Magic Number replacement
   */
  public static final int MAX_OCCUPANCY_DOUBLE = 2;

  /**
   * Constructs a new DoubleRoom with the given price.
   * @param price the price per night for the room
   */
  public DoubleRoom(double price) {
    super(MAX_OCCUPANCY_DOUBLE, price);
  }
}
