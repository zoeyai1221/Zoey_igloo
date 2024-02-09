package hw2;

/**
 * Represents a single room in a hotel.
 */
public class SingleRoom extends Room {
  /**
   * Magic Number replacement
   */
  public static final int MAX_OCCUPANCY_SINGLE = 1;

  /**
   * Constructs a new SingleRoom with the given price.
   * @param price the price per night for the room
   */
  public SingleRoom(double price) {
    super(MAX_OCCUPANCY_SINGLE, price);
  }
}
