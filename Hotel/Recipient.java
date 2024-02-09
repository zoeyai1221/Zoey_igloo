package hw2;

/**
 * Represents a recipient of mail.
 */
public class Recipient {
  private final String firstName;
  private final String lastName;
  private final String email;

  /**
   * Constructs a new Recipient with the given first name, last name, and email address.
   * @param firstName the first name of the recipient
   * @param lastName the last name of the recipient
   * @param email the email address of the recipient
   * @throws IllegalArgumentException if any of the parameters are null or empty
   */
  public Recipient(String firstName, String lastName, String email) {
    if (firstName == null || lastName == null || email == null || firstName.isEmpty() || lastName.isEmpty() || email.isEmpty()) {
      throw new IllegalArgumentException("First name, last name, and email address cannot be null or empty");
    }
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
  }

  /**
   * Gets the firstName of the recipient.
   * @return the firstName
   */
  public String getFirstName() {
    return firstName;
  }

  /**
   * Gets the lastName of the recipient.
   * @return the lastName
   */
  public String getLastName() {
    return lastName;
  }

  /**
   * Gets the email of the recipient.
   * @return the email
   */
  public String getEmail() {
    return email;
  }

  @Override
  public String toString() {
    return firstName + " " + lastName + " Email:" + email;
  }
}
