#ifndef SCORE_H
#define SCORE_H

#include <QMainWindow>

namespace Ui {
class Score;
}

class Score : public QMainWindow
{
    Q_OBJECT

public:
    explicit Score(QWidget *parent = 0);
    ~Score();

private:
    Ui::Score *ui;
};

#endif // SCORE_H
