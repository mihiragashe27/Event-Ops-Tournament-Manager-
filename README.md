# Event & Tournament Leaderboard Manager

A lightweight, Object-Oriented Python application designed to streamline tournament score tracking and automated leaderboard generation for college events and esports competitions.

This project bridges hands-on event operations experience with core computer science concepts, utilizing NumPy for fast array manipulation and score averaging.

---

## Key Features

- **Object-Oriented Design:** Clean encapsulation separating player entities (`Participant`) from tournament management operations (`EventManager`).
- **Dynamic Leaderboard Ranking:** Uses NumPy's `np.argsort()` to sort participants in real-time based on their current average scores.
- **Automated Score Aggregation:** Leverages `np.mean()` to calculate average performances across multiple matches instantly.
- **Fail-Safe Checks:** Gracefully handles participants with no recorded scores without crashing the program.

---

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** NumPy
- **Paradigm:** Object-Oriented Programming (OOP)

---

## Project Structure

- `Participant`: Class responsible for storing individual participant names and their list of match scores.
- `EventManager`: Class responsible for managing registered participants, logging incoming scores, computing statistics, and displaying formatted rankings.

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Event-Ops-Tournament-Manager.git](https://github.com/YOUR_USERNAME/Event-Ops-Tournament-Manager.git)
   cd Event-Ops-Tournament-Manager
