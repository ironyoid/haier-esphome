#pragma once

#include "esphome/components/select/select.h"
#include "../haier_base.h"

namespace esphome {
namespace haier {

class SleepTimerSelect : public select::Select, public Parented<HaierClimateBase> {
 public:
  SleepTimerSelect() = default;

 protected:
  void control(const std::string &value) override;
};

}  // namespace haier
}  // namespace esphome
