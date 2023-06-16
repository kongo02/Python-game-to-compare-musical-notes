import random


NOTES = {
    "A": 0, "A#": 1, "Bb": 1, "B": 2,
    "C": 3, "C#": 4, "Db": 4, "D": 5,
    "D#": 6, "Eb": 6, "E": 7, "F": 8,
    "F#": 9, "Gb": 9, "G": 10, "G#": 11,
    "Ab": 11
}


def generate_notes():
    """Generate two random notes."""
    notes = random.sample(list(NOTES), k=2)
    return notes


def calculate_semitones(note1, note2):
    """Calculate the number of semitones between two notes."""
    num_semitones = (NOTES[note2] - NOTES[note1]) % 12
    return num_semitones


def play_game():
    """Play the game."""
    print("Welcome to the Guess the Semitones game!\n")

    while True:
        note1, note2 = generate_notes()
        num_semitones = calculate_semitones(note1, note2)

        while True:
            guess = input(f"\nGuess how many semitones are between {note1} and {note2} "
                          "(or enter 'give up' to see the answer): ").strip().lower()

            if guess == "give up":
                print(f"\nThe correct answer is {num_semitones}.\n")
                break

            try:
                guess = int(guess)
                if guess == num_semitones:
                    print("\nCorrect!\n")
                    break
                else:
                    print("\nIncorrect. Try again.\n")
            except ValueError:
                print("\nInvalid input. Please enter a valid number, "
                      "or enter 'give up' to see the answer.\n")

        while True:
            choice = input(
                "Do you want to play again? (Y/N): ").strip().lower()
            if choice in ["y", "n"]:
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if choice == "n":
            print("\nThanks for playing!")
            break


def test_generate_notes():
    """Test if the notes generated are valid."""
    notes = generate_notes()
    assert len(notes) == 2
    assert notes[0] != notes[1]  # Test that the two notes are not the same
    for note in notes:
        assert note in NOTES

    # Test edge case where the same note is generated twice
    same_note = generate_notes()
    while same_note[0] != same_note[1]:
        same_note = generate_notes()
    assert same_note[0] == same_note[1]



def test_calculate_semitones():
    """Test the calculation of semitones between notes."""
    assert calculate_semitones("C", "C") == 0
    assert calculate_semitones("C", "D") == 2
    assert calculate_semitones("C#", "D") == 1
    assert calculate_semitones("C#", "Db") == 0
    assert calculate_semitones("B", "C") == 1
    assert calculate_semitones("Ab", "B") == 1
    assert calculate_semitones("A", "G#") == 1
    assert calculate_semitones("C", "B") == 11
    assert calculate_semitones("F#", "G") == 1

    # Test edge case where the two notes are the same
    assert calculate_semitones("G#", "G#") == 0



if __name__ == "__main__":
    play_game()
