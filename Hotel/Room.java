package hw2;

import java.util.Objects;

/**
 * Abstract base class representing a room in a hotel.
 */
public abstract class Room {

  // Magic Number replacement
  public static final int MIN_PRICE = 0;
  public static final int MIN_NUM_OF_GUEST = 0;

  // Constants for maximum occupancy
  private final int maxOccupancy;
  // Price per night
  private final double price;
  // Number of guests currently assigned to the room
  private int numberOfGuests;

  /**
   * Constructs a new Room with the given maximum occupancy and price.
   * @param maxOccupancy the maximum occupancy of the room
   * @param price the price per night for the room
   * @throws IllegalArgumentException if price is negative
   */
  public Room(int maxOccupancy, double price) {
    if (price < MIN_PRICE) {
      throw new IllegalArgumentException("Price cannot be negative");
    }
    this.maxOccupancy = maxOccupancy;
    this.price = price;
    this.numberOfGuests = MIN_NUM_OF_GUEST;
  }

  /**
   * Checks if the room is available.
   * @return true if the room is available, false otherwise
   */
  public boolean isAvailable() {
    return numberOfGuests == MIN_NUM_OF_GUEST;
  }

  /**
   * Books the room for the specified number of guests.
   * @param numGuests the number of guests to book the room for
   * @throws IllegalStateException if the room is not available or the number of guests exceeds the maximum occupancy
   */
  public void bookRoom(int numGuests) {
    if (!isAvailable() || numGuests <= MIN_NUM_OF_GUEST || numGuests > maxOccupancy) {
      throw new IllegalStateException("Invalid booking");
    }
    numberOfGuests = numGuests;
  }

  /**
   * Gets the number of guests currently assigned to the room.
   * @return the number of guests
   */
  public int getNumberOfGuests() {
    return numberOfGuests;
  }

  /**
   * Gets the maximum occupancy of the room.
   * @return the maximum occupancy
   */
  public int getMaxOccupancy() {
    return maxOccupancy;
  }

  /**
   * Gets the price per night for the room.
   * @return the price
   */
  public double getPrice() {
    return price;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Room room = (Room) o;
    return Double.compare(room.price, price) == 0 &&
        numberOfGuests == room.numberOfGuests;
  }

  @Override
  public int hashCode() {
    return Objects.hash(price, numberOfGuests);
  }

}
