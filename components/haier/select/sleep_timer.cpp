#include "sleep_timer.h"

namespace esphome {
namespace haier {

void SleepTimerSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_sleep_timer(value);
}

}  // namespace haier
}  // namespace esphome
