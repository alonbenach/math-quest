from __future__ import annotations

import ipywidgets as widgets

from exercises import dropdown_question, numeric_question, vector_question


def render_practice_checkpoints() -> widgets.VBox:
    checkpoints = [
        numeric_question(
            prompt="1. Compute [2, 3] . [4, 5]",
            expected=23,
            hint="Not quite yet. Multiply matching entries and then add the results.",
            success_message="Correct. 2*4 + 3*5 = 23.",
        ),
        numeric_question(
            prompt="2. Compute [1, -1] . [1, 1]",
            expected=0,
            hint="Not quite yet. Watch the sign on the second product.",
            success_message="Correct. The dot product is 0, so the vectors are orthogonal.",
        ),
        dropdown_question(
            prompt="3. If two nonzero vectors have dot product 0, how should you classify their directions?",
            options=["same-ish direction", "perpendicular", "opposite-ish direction"],
            expected="perpendicular",
            hint="Not quite yet. A zero dot product means the vectors meet at a right angle.",
            success_message="Correct. Zero dot product means the vectors are perpendicular, also called orthogonal.",
        ),
        vector_question(
            prompt="4. Compute the matrix-vector product [[2, 0], [1, -1]] @ [3, 4]",
            expected=[6, -1],
            hint="Not quite yet. Compute one row at a time and return the result as a vector.",
            success_message="Correct. The output vector is [6, -1].",
        ),
    ]
    return widgets.VBox(checkpoints)

