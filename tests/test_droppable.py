from pages.droppable_page import DroppablePage


def test_drag_and_drop(page):
    droppable = DroppablePage(page)
    droppable.goto()
    
    # check the initial text in the droppable area
    assert droppable.get_droppable_area_text() == "Drop here"

    # drag and drop
    droppable.drag_element_to_droppable_area()
    assert droppable.droppable_area_has_text("Dropped!")