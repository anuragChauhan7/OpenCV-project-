
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            #CHECK IF OBJECT IS DETECTED ALREADY
            same_object_detected = False

            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 70:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True

                    #START TIMER
                    if (y >= 410 and y <= 430):
                        self.s1[0,id] = time.time()

                    #STOP TIMER and FIND DIFFERENCE
                    if (y >= 235 and y <= 255):
                        self.s2[0,id] = time.time()


