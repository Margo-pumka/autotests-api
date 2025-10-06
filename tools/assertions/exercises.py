import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExerciseResponseSchema, ExerciseSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


@allure.step("Assert create exercise response")
def assert_create_exercise_response(
        create_exercise_request: CreateExerciseRequestSchema,
        create_exercise_response: GetExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует данным из запроса.

    :param create_exercise_request: Исходный запрос на создание упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(create_exercise_request.title, create_exercise_response.exercise.title, "title")
    assert_equal(create_exercise_request.course_id, create_exercise_response.exercise.course_id, "course_id")
    assert_equal(create_exercise_request.max_score, create_exercise_response.exercise.max_score, "max_score")
    assert_equal(create_exercise_request.min_score, create_exercise_response.exercise.min_score, "min_score")
    assert_equal(create_exercise_request.order_index, create_exercise_response.exercise.order_index, "order_index")
    assert_equal(create_exercise_request.description, create_exercise_response.exercise.description, "description")
    assert_equal(create_exercise_request.estimated_time, create_exercise_response.exercise.estimated_time, "estimated_time")


@allure.step("Assert exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Assert get exercise response")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение упражнения соответствует данным из ответа создания упражнения.

    :param get_exercise_response: Ответ API при получении упражнения.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Assert update exercise response")
def assert_update_exercise_response(
        update_exercise_request: UpdateExerciseRequestSchema,
        update_exercise_response: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param update_exercise_request: Исходный запрос на обновление упражнения.
    :param update_exercise_response: Ответ API при обновлении упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(update_exercise_response.exercise.title, update_exercise_request.title,  "title")
    assert_equal(update_exercise_response.exercise.max_score, update_exercise_request.max_score,  "max_score")
    assert_equal(update_exercise_response.exercise.min_score, update_exercise_request.min_score,  "min_score")
    assert_equal(update_exercise_response.exercise.order_index, update_exercise_request.order_index,  "order_index")
    assert_equal(update_exercise_response.exercise.description, update_exercise_request.description,  "description")
    assert_equal(
        update_exercise_response.exercise.estimated_time, update_exercise_request.estimated_time, "estimated_time")


@allure.step("Assert exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упражнение не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "File not found"
     """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


@allure.step("Assert get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[GetExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка упражнений соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка упражнений.
    :param create_exercise_responses: Список API ответов при создании упражнений.
    :raises AssertionError: Если данные упражнений не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)
