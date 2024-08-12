from PyQt6.QtWidgets import *

app =  QApplication([])
window = QWidget()

text_edit = QTextEdit()
list_notes_lbl = QLabel("")
notes_list = QListWidget()
create_note_btn = QPushButton()
delete_note_btn = QPushButton()
save_note_btn = QPushButton()
list_teg_lbl = QListWidget()
teg_list = QListWidget()
create_teg = QLineEdit()
add_teg_btn = QPushButton()
save_note_btn = QPushButton()





main_line = QHBoxLayout()
main_line.addWidget(text_edit)


v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v1.addWidget(create_note_btn)
v1.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addWidget(list_teg_lbl)
v1.addWidget(teg_list)
v1.addWidget(create_teg)
v1.addWidget(add_teg_btn)
v1.addWidget(save_note_btn)

main_line.addLayout(v1)






window.setLayout(main_line)
window.show()
app.exec()