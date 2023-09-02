from Model import PhoneBook
import Text
import View

def search_contact(pb):
    word = View.input_request(Text.input_search_word)
    result = pb.find_contact(word)
    View.show_book(result, Text.not_find(word))
    if result:
        return True

def start():
    pb = PhoneBook()
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                pb.open_file()
                print(pb.phone_book)
                View.print_message(Text.load_successful)
            case 2:
                pb.save_file()
                View.print_message(Text.save_successful)
            case 3:
                View.show_book(pb, Text.empty_book_error)
            case 4:
                new_contact = View.input_contact(Text.input_contact())
                pb.add_contact(new_contact)
                View.print_message(Text.contact_action(new_contact[0], Text.operation[0]))
            case 5:
                search_contact(pb)
            case 6:
                if search_contact(pb):
                    c_id = int(View.input_request(Text.input_edit_contact_id))
                    new_contact = View.input_contact(Text.input_contact(True))
                    name = pb.edit_contact(c_id, new_contact)
                    View.print_message(Text.contact_action(name, Text.operation[1]))
            case 7:
                if search_contact(pb):
                    c_id = int(View.input_request(Text.input_del_contact_id))
                    name = pb.delete_contact(c_id)
                    View.print_message(Text.contact_action(name, Text.operation[2]))
            case 8:
                if pb.original_book != pb.phone_book:
                    if View.input_request(Text.confirm_changes).lower() == 'y':
                        pb.save_file()
                        View.print_message(Text.save_successful)
                View.print_message(Text.exit_program)
                break

