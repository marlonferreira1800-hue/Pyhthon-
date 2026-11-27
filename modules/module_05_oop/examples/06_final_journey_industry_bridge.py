"""Module 5 (Ch. 23) — Final Remarks: Bridge to Data Science, ML, and Engineering.

Mini object-oriented pipeline showing how classes, encapsulation, and
polymorphism underpin modern libraries like scikit-learn, pandas, and web APIs.
"""


class BasePredictiveModel:
    """scikit-learn-inspired interface demonstrating model polymorphism."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._fitted = False

    def fit(self, data: list[float]) -> "BasePredictiveModel":
        raise NotImplementedError("Subclasses must implement fit().")

    def predict(self, value: float) -> float:
        raise NotImplementedError("Subclasses must implement predict().")


class MovingAverageModel(BasePredictiveModel):
    """Predicts next value by blending the historical mean with the input."""

    def __init__(self) -> None:
        super().__init__("Simple Mean")
        self._mean = 0.0

    def fit(self, data: list[float]) -> "MovingAverageModel":
        if not data:
            raise ValueError("Training dataset cannot be empty.")
        self._mean = sum(data) / len(data)
        self._fitted = True
        return self

    def predict(self, value: float) -> float:
        if not self._fitted:
            raise RuntimeError("Model has not been fitted yet.")
        return round((self._mean + value) / 2, 2)


class LinearTrendModel(BasePredictiveModel):
    """Estimates average growth ratio across consecutive observations."""

    def __init__(self, default_factor: float = 1.05) -> None:
        super().__init__("Linear Trend")
        self._factor = default_factor

    def fit(self, data: list[float]) -> "LinearTrendModel":
        if len(data) < 2:
            raise ValueError("At least 2 data points are required.")
        ratios = [data[i] / data[i - 1] for i in range(1, len(data)) if data[i - 1] > 0]
        if ratios:
            self._factor = sum(ratios) / len(ratios)
        self._fitted = True
        return self

    def predict(self, value: float) -> float:
        if not self._fitted:
            raise RuntimeError("Model has not been fitted yet.")
        return round(value * self._factor, 2)


def demonstrate_industry_bridge() -> None:
    rental_history = [100.0, 110.0, 121.0, 133.1]
    models: list[BasePredictiveModel] = [
        MovingAverageModel(),
        LinearTrendModel(),
    ]
    print("=== Bridge: OOP -> Machine Learning & Software Engineering ===")
    for model in models:
        model.fit(rental_history)
        forecast = model.predict(133.1)
        print(f"Model '{model.name}' -> next period forecast: {forecast}")


if __name__ == "__main__":
    demonstrate_industry_bridge()
