#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def summarize(x):
    return {
        "n": len(x),
        "mean": np.mean(x),
        "median": np.median(x),
        "std": np.std(x, ddof=1),
        "min": np.min(x),
        "max": np.max(x),
    }


def main():
    rng = np.random.default_rng(576)
    sample = rng.normal(loc=100, scale=15, size=50)

    print("Summary statistics for a simulated sample:")
    for name, value in summarize(sample).items():
        print(f"  {name:>6}: {value:.3f}")


if __name__ == "__main__":
    main()