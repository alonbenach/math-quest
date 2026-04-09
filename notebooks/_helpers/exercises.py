from __future__ import annotations

import ast
from typing import Iterable, Sequence

import ipywidgets as widgets
from IPython.display import display


SUCCESS_STYLE = {"description_width": "initial"}


def _feedback_html(message: str, color: str) -> widgets.HTML:
    return widgets.HTML(
        value=f"<div style='margin-top:8px; color:{color}; font-weight:600;'>{message}</div>"
    )


def _render_result(output: widgets.Output, message: str, ok: bool) -> None:
    color = "#1a7f37" if ok else "#b42318"
    with output:
        output.clear_output()
        display(_feedback_html(message, color))


def numeric_question(
    prompt: str,
    expected: float,
    *,
    hint: str = "Not quite yet. Recheck your arithmetic.",
    success_message: str = "Correct.",
    tolerance: float | None = None,
    answer_label: str = "Your answer:",
) -> widgets.VBox:
    prompt_html = widgets.HTML(f"<b>{prompt}</b>")
    answer = widgets.Text(
        placeholder="Enter a number",
        description=answer_label,
        style=SUCCESS_STYLE,
    )
    check = widgets.Button(description="Check Answer", button_style="primary")
    output = widgets.Output()

    def on_click(_: widgets.Button) -> None:
        raw = answer.value.strip()
        try:
            value = float(raw)
        except ValueError:
            _render_result(output, "Please enter a numeric value, for example `23` or `4.5`.", False)
            return

        if tolerance is None:
            is_correct = value == expected
        else:
            is_correct = abs(value - expected) <= tolerance

        if is_correct:
            _render_result(output, success_message, True)
        else:
            _render_result(output, hint, False)

    check.on_click(on_click)
    return widgets.VBox([prompt_html, answer, check, output])


def vector_question(
    prompt: str,
    expected: Sequence[float],
    *,
    hint: str = "Not quite yet. Recheck each component.",
    success_message: str = "Correct.",
    answer_label: str = "Your answer:",
) -> widgets.VBox:
    prompt_html = widgets.HTML(f"<b>{prompt}</b>")
    answer = widgets.Text(
        placeholder="Example: [6, -1]",
        description=answer_label,
        style=SUCCESS_STYLE,
        layout=widgets.Layout(width="420px"),
    )
    check = widgets.Button(description="Check Answer", button_style="primary")
    output = widgets.Output()
    expected_list = list(expected)

    def on_click(_: widgets.Button) -> None:
        raw = answer.value.strip()
        try:
            parsed = ast.literal_eval(raw)
        except (ValueError, SyntaxError):
            _render_result(output, "Use Python-style list format, for example `[6, -1]`.", False)
            return

        if not isinstance(parsed, (list, tuple)):
            _render_result(output, "Please enter a list like `[6, -1]`.", False)
            return

        try:
            values = [float(item) for item in parsed]
        except (TypeError, ValueError):
            _render_result(output, "Each vector entry should be numeric.", False)
            return

        if values == [float(item) for item in expected_list]:
            _render_result(output, success_message, True)
        else:
            _render_result(output, hint, False)

    check.on_click(on_click)
    return widgets.VBox([prompt_html, answer, check, output])


def dropdown_question(
    prompt: str,
    options: Iterable[str],
    expected: str,
    *,
    hint: str = "Not quite yet. Revisit the sign of the dot product.",
    success_message: str = "Correct.",
    answer_label: str = "Choose one:",
) -> widgets.VBox:
    prompt_html = widgets.HTML(f"<b>{prompt}</b>")
    answer = widgets.Dropdown(
        options=list(options),
        value=None,
        description=answer_label,
        style=SUCCESS_STYLE,
    )
    check = widgets.Button(description="Check Answer", button_style="primary")
    output = widgets.Output()

    def on_click(_: widgets.Button) -> None:
        if answer.value is None:
            _render_result(output, "Please choose one of the answer options first.", False)
            return

        if answer.value == expected:
            _render_result(output, success_message, True)
        else:
            _render_result(output, hint, False)

    check.on_click(on_click)
    return widgets.VBox([prompt_html, answer, check, output])
