def abs_path_from_project(relative_path: str):
    import lesson_5_23_mobile_autotests_with_Browserstack
    from pathlib import Path

    return (
        Path(lesson_5_23_mobile_autotests_with_Browserstack.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )