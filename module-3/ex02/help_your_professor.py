def average(class_notes: dict[str, int]) -> float:
    """Calculates the average score from a dictionary of class notes."""
    if len(class_notes) == 0:
        return 0
    return (sum(class_notes.values()) / len(class_notes))