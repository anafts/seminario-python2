def table_statistics(table,title):
  new_player_statistics = sorted(table.items(), key=lambda x: x[1]['score'], reverse=True)

  print(f"{title}:")
  print(f"{'Cocinero':<15} {'Puntaje':<10} {'Rondas ganadas':<18} {'Mejor ronda':<15} {'Promedio':<10}")
  print("-" * 70)

  for player, statistic in new_player_statistics:
      print(f"{player:<15} {statistic['score']:<10} {statistic['wins']:<18} {statistic['best']:<15} {statistic['mean']:<10.1f}")

  print("-" * 70)